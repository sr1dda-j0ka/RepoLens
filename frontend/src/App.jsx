import { useState } from "react";
import api from "./api/api";
import Navbar from "./components/Navbar";
import RepoInput from "./components/RepoInput";
import ChatInput from "./components/ChatInput";
import ChatHistory from "./components/ChatHistory";
import AnswerPanel from "./components/AnswerPanel";
import RepoOverview from "./components/RepoOverview";

function App() {
  const [repoURL, setURL] = useState("");
  const [loading, setLoading] = useState(false);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [summary, setSummary] = useState("");
  const [folderTree, setFolderTree] = useState("");
  const [stats, setStats] = useState(null);

  const loadRepo = async () => {
    setLoading(true);

    try {
      const res = await api.post("/repo-request", {
        repo_url: repoURL,
      });

      setSummary(res.data.summary);
      setFolderTree(res.data.folder_tree);
      setStats(res.data.stats);

      alert(res.data.message);
    } catch (err) {
      alert("Failed to load repo");
      console.log(err);
    }

    setLoading(false);
  };

  const askQuestion = async () => {
    try {
      const res = await api.get("/ask", {
        params: {
          question: question,
        },
      });

      setAnswer(res.data.answer);
      setSources(res.data.sources);
    } catch (err) {
      alert("Error asking question");
      console.log(err);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <Navbar />

      <div className="max-w-screen-2xl mx-auto p-6">

        <h1 className="text-4xl font-bold mb-2">
          Analyze Any Repository
        </h1>

        <p className="text-slate-400 mb-8">
          AI-powered repository onboarding and semantic code search.
        </p>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">

          {/* LEFT SIDEBAR */}

          <div className="lg:col-span-3">

            <div className="sticky top-24">

              <ChatHistory />

            </div>

          </div>

          {/* MAIN CONTENT */}

          <div className="lg:col-span-9 flex flex-col gap-6">

            <RepoInput
              repoURL={repoURL}
              setURL={setURL}
              loading={loading}
              loadRepo={loadRepo}
            />

            <RepoOverview
              summary={summary}
              folderTree={folderTree}
              stats={stats}
            />

            <ChatInput
              question={question}
              setQuestion={setQuestion}
              askQuestion={askQuestion}
            />

            <AnswerPanel
              answer={answer}
              sources={sources}
            />

          </div>

        </div>

      </div>
    </div>
  );
}

export default App;

