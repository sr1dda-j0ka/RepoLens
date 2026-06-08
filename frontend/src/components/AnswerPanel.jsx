export default function AnswerPanel({ answer, sources }) {
  return (
    <div
      className="
      bg-slate-900
      border
      border-slate-800
      rounded-2xl
      p-6
      min-h-[400px]
    "
    >
      <h2 className="text-lg font-semibold mb-4">Answer</h2>

      <p className="text-slate-300 whitespace-pre-wrap leading-7">{answer}</p>

      <div className="mt-6 flex gap-2 flex-wrap">
        {sources.map((source, index) => (
          <span
            key={index}
            className="
                bg-slate-800
                px-3
                py-1
                rounded-full
                text-blue-400
                text-sm
              "
          >
            {source}
          </span>
        ))}
      </div>
    </div>
  );
}
