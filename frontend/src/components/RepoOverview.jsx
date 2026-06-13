import { useState } from "react";

import {
  FolderTree,
  FileCode2,
  BrainCircuit,
  Boxes,
  Wrench,
  ChevronDown,
  ChevronUp,
} from "lucide-react";

export default function RepoOverview({ summary, folderTree, stats }) {
  const [open, setOpen] = useState(false);

  if (!summary || !stats) {
    return null;
  }

  return (
    <div
      className="
        bg-slate-900
        border
        border-slate-800
        rounded-2xl
        p-8
        shadow-xl
      "
    >
      {/* HEADER */}

      <div
        onClick={() => setOpen(!open)}
        className="
          flex
          justify-between
          items-center
          cursor-pointer
        "
      >
        <div className="flex items-center gap-3">
          <div
            className="
              p-3
              rounded-xl
              bg-blue-600/20
            "
          >
            <BrainCircuit size={24} className="text-blue-400" />
          </div>

          <div>
            <h2 className="text-2xl font-bold">Repository Overview</h2>

            <p className="text-slate-400 text-sm">
              AI generated project analysis
            </p>
          </div>
        </div>

        {open ? (
          <ChevronUp className="text-slate-400" />
        ) : (
          <ChevronDown className="text-slate-400" />
        )}
      </div>

      {/* COLLAPSIBLE CONTENT */}

      <div
        className={`
          overflow-hidden
          transition-all
          duration-500
          ease-in-out
          ${open ? "max-h-[5000px] mt-8" : "max-h-0"}
        `}
      >
        {/* SUMMARY */}

        <div className="mb-8">
          <h3
            className="
              flex
              items-center
              gap-2
              text-blue-400
              font-semibold
              mb-3
            "
          >
            <Boxes size={18} />
            Summary
          </h3>

          <div
            className="
              bg-slate-950
              border
              border-slate-800
              rounded-xl
              p-5
            "
          >
            <p
              className="
                whitespace-pre-wrap
                text-slate-300
                leading-8
              "
            >
              {summary}
            </p>
          </div>
        </div>

        {/* STATS */}

        <div className="mb-8">
          <h3
            className="
              flex
              items-center
              gap-2
              text-blue-400
              font-semibold
              mb-3
            "
          >
            <FileCode2 size={18} />
            Repository Stats
          </h3>

          <div className="grid grid-cols-2 gap-5">
            <div
              className="
                bg-slate-950
                border
                border-slate-800
                rounded-xl
                p-5
              "
            >
              <p className="text-slate-400">Files</p>

              <p className="text-3xl font-bold mt-2">{stats.files}</p>
            </div>

            <div
              className="
                bg-slate-950
                border
                border-slate-800
                rounded-xl
                p-5
              "
            >
              <p className="text-slate-400">Folders</p>

              <p className="text-3xl font-bold mt-2">{stats.folders}</p>
            </div>
          </div>
        </div>

        {/* LANGUAGES */}

        <div className="mb-8">
          <h3
            className="
              flex
              items-center
              gap-2
              text-blue-400
              font-semibold
              mb-3
            "
          >
            <Wrench size={18} />
            Languages
          </h3>

          <div
            className="
              bg-slate-950
              border
              border-slate-800
              rounded-xl
              p-5
            "
          >
            <div
              className="
                flex
                h-3
                rounded-full
                overflow-hidden
                mb-6
              "
            >
              {Object.entries(stats.languages).map(([lang, pct], i) => {
                const colors = [
                  "bg-blue-500",
                  "bg-yellow-500",
                  "bg-green-500",
                  "bg-red-500",
                  "bg-purple-500",
                  "bg-pink-500",
                ];

                return (
                  <div
                    key={lang}
                    className={colors[i % colors.length]}
                    style={{
                      width: `${pct}%`,
                    }}
                  />
                );
              })}
            </div>

            <div className="space-y-3">
              {Object.entries(stats.languages).map(([lang, pct]) => (
                <div
                  key={lang}
                  className="
                    flex
                    justify-between
                  "
                >
                  <span className="text-slate-300">{lang}</span>

                  <span className="text-blue-400">{pct}%</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* PROJECT STRUCTURE */}

        <div>
          <h3
            className="
              flex
              items-center
              gap-2
              text-blue-400
              font-semibold
              mb-3
            "
          >
            <FolderTree size={18} />
            Project Structure
          </h3>

          <pre
            className="
              bg-slate-950
              border
              border-slate-800
              rounded-xl
              p-5
              overflow-auto
              text-sm
              text-slate-300
              max-h-[500px]
            "
          >
            {folderTree}
          </pre>
        </div>
      </div>
    </div>
  );
}
