import { motion, AnimatePresence } from "framer-motion";
import { FaGithub } from "react-icons/fa";
import ProgressBar from "./ProgressBar";
import StageItem from "./StageItem";

const STAGES = [
  "Cloning Repository",
  "Scanning Source Files",
  "Generating Code Chunks",
  "Generating Embeddings",
  "Building Search Index",
  "Generating Repository Summary",
  "Completed",
];

export default function LoadingOverlay({ loading, progress }) {
  return (
    <AnimatePresence>
      {loading && (
        <motion.div
          className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 backdrop-blur-md"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
        >
          <motion.div
            initial={{
              scale: 0.92,
              opacity: 0,
              y: 25,
            }}
            animate={{
              scale: 1,
              opacity: 1,
              y: 0,
            }}
            exit={{
              scale: 0.95,
              opacity: 0,
            }}
            transition={{
              duration: 0.35,
            }}
            className="
              w-[650px]
              rounded-3xl
              bg-slate-900
              border
              border-slate-800
              shadow-[0_0_60px_rgba(37,99,235,0.15)]
              p-8
            "
          >
            {/* Header */}

            <div className="flex items-center gap-3 mb-8">
              <FaGithub className="text-3xl text-blue-400" />

              <div>
                <h2 className="text-2xl font-bold">
                  RepoAnalyser
                </h2>

                <p className="text-slate-400 text-sm">
                  Semantic Repository Indexing
                </p>
              </div>
            </div>

            {/* Current Stage */}

            <div className="mb-6">
              <h3 className="text-lg font-semibold">
                {progress.stage}
              </h3>

              <p className="text-slate-400 text-sm mt-1">
                Building a semantic search index for the repository.
                This may take several minutes for very large repositories.
              </p>
            </div>

            {/* Progress */}

            <ProgressBar progress={progress.progress} />

            {/* Files */}

            <div className="flex gap-8 mt-8 text-sm">

              <div>
                <p className="text-slate-500">
                  Files
                </p>

                <p className="text-xl font-semibold">
                  {progress.files}
                </p>
              </div>

              <div>
                <p className="text-slate-500">
                  Chunks
                </p>

                <p className="text-xl font-semibold">
                  {progress.chunks}
                </p>
              </div>

            </div>

            {/* Stage List */}

            <div className="mt-8 space-y-3">

              {STAGES.map((stage) => (

                <StageItem
                  key={stage}
                  stage={stage}
                  currentStage={progress.stage}
                />

              ))}

            </div>

          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}