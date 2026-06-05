export default function AnswerPanel() {
  return (
    <div className="
      bg-slate-900
      border
      border-slate-800
      rounded-2xl
      p-6
      min-h-[400px]
    ">
      <h2 className="text-lg font-semibold mb-4">
        Answer
      </h2>

      <p className="text-slate-300">
        AI response will appear here.
      </p>

      <div className="mt-6 flex gap-2 flex-wrap">

        <span className="
          bg-slate-800
          px-3
          py-1
          rounded-full
          text-blue-400
        ">
          app.py
        </span>

      </div>
    </div>
  );
}