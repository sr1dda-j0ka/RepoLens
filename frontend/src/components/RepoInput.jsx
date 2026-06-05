export default function RepoInput() {
  return (
    <div className="
      bg-slate-900
      border
      border-slate-800
      rounded-2xl
      p-6
    ">
      <h2 className="text-lg font-semibold mb-4">
        Load Repository
      </h2>

      <div className="flex gap-3 flex-wrap">

        <input
          type="text"
          placeholder="Github Repository URL"
          className="
            flex-1
            bg-slate-950
            border
            border-slate-700
            rounded-xl
            px-4
            py-3
          "
        />

        <button className="
          bg-blue-600
          px-5
          rounded-xl
          min-h-[45px]
        ">
          Load
        </button>

      </div>
    </div>
  );
}