export default function ChatInput({ question, setQuestion, askQuestion }) {
  return (
    <div
      className="
      bg-slate-900
      border
      border-slate-800
      rounded-2xl
      p-6
    "
    >
      <h2 className="text-lg font-semibold mb-4">Ask Repository</h2>

      <textarea
        rows="4"
        placeholder="How does routing work?"
        value={question}
        onChange={(e) => {
          setQuestion(e.target.value);
        }}
        className="
          w-full
          bg-slate-950
          border
          border-slate-700
          rounded-xl
          p-4
        "
      />

      <button
        onClick={askQuestion}
        className="
        mt-4
        bg-blue-600
        px-5
        py-3
        rounded-xl
      "
      >
        Ask
      </button>
    </div>
  );
}
