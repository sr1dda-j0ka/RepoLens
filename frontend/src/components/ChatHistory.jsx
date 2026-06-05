export default function ChatHistory() {
  return (
    <div className="
      bg-slate-900
      border
      border-slate-800
      rounded-2xl
      p-6
      h-full
    ">
      <h2 className="font-semibold mb-4">
        Chat History
      </h2>

      <div className="space-y-3">

        <div className="
          bg-slate-800
          p-3
          rounded-xl
          cursor-pointer
        ">
          How does routing work?
        </div>

        <div className="
          bg-slate-800
          p-3
          rounded-xl
          cursor-pointer
        ">
          What is a blueprint?
        </div>

      </div>
    </div>
  );
}