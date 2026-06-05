import Navbar from "./components/Navbar";
import RepoInput from "./components/RepoInput";
import ChatInput from "./components/ChatInput";
import ChatHistory from "./components/ChatHistory";
import AnswerPanel from "./components/AnswerPanel";

function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">

      <Navbar />

      <div className="max-w-7xl mx-auto p-6">

        <h1 className="text-4xl font-bold mb-2">
          Analyze Any Repository
        </h1>

        <p className="text-slate-400 mb-8">
          Ask questions about any GitHub codebase.
        </p>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">

          <div className="order-2 md:order-1 col-span-3">
            <ChatHistory />
          </div>

          <div className="order-1 lg:order-2 lg:col-span-9 flex flex-col gap-6">
            <RepoInput />
            <ChatInput />
            <AnswerPanel />
          </div>

        </div>

      </div>

    </div>
  );
}

export default App;