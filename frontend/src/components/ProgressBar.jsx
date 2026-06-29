import { motion } from "framer-motion";

export default function ProgressBar({ progress }) {
  return (
    <div className="mt-6">

      <div className="flex justify-between mb-2">

        <span className="text-sm text-slate-400">
          Overall Progress
        </span>

        <motion.span
          key={progress}
          initial={{ opacity: 0, y: -5 }}
          animate={{ opacity: 1, y: 0 }}
          className="font-semibold text-blue-400"
        >
          {progress}%
        </motion.span>

      </div>

      <div
        className="
          relative
          h-4
          w-full
          overflow-hidden
          rounded-full
          bg-slate-800
        "
      >

        <motion.div

          initial={{ width: 0 }}

          animate={{
            width: `${progress}%`,
          }}

          transition={{
            duration: 0.45,
            ease: "easeInOut",
          }}

          className="
            h-full
            rounded-full
            bg-gradient-to-r
            from-cyan-400
            via-blue-500
            to-indigo-600
          "
        />

        {/* Moving glow */}

        <motion.div

          animate={{
            x: ["-100%", "250%"],
          }}

          transition={{
            duration: 2,
            repeat: Infinity,
            ease: "linear",
          }}

          className="
            absolute
            top-0
            left-0
            h-full
            w-16
            bg-white/20
            blur-sm
          "
        />

      </div>

    </div>
  );
}