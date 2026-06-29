import { motion } from "framer-motion";
import {
  FaCheckCircle,
  FaRegCircle,
} from "react-icons/fa";

import { ImSpinner2 } from "react-icons/im";

const STAGES = [
  "Cloning Repository",
  "Scanning Source Files",
  "Generating Code Chunks",
  "Generating Embeddings",
  "Building Search Index",
  "Generating Repository Summary",
  "Completed",
];

export default function StageItem({
  stage,
  currentStage,
}) {

  const currentIndex = STAGES.indexOf(currentStage);
  const stageIndex = STAGES.indexOf(stage);

  const completed = stageIndex < currentIndex;
  const active = stageIndex === currentIndex;

  return (

    <motion.div

      layout

      initial={{
        opacity: 0,
        x: -15,
      }}

      animate={{
        opacity: 1,
        x: 0,
      }}

      transition={{
        duration: 0.25,
      }}

      className="flex items-center gap-3"

    >

      {/* Icon */}

      {completed ? (

        <motion.div

          initial={{
            scale: 0,
          }}

          animate={{
            scale: 1,
          }}

          transition={{
            type: "spring",
            stiffness: 250,
          }}

        >

          <FaCheckCircle
            className="text-green-400 text-lg"
          />

        </motion.div>

      ) : active ? (

        <motion.div

          animate={{
            rotate: 360,
          }}

          transition={{
            repeat: Infinity,
            duration: 1,
            ease: "linear",
          }}

        >

          <ImSpinner2
            className="text-blue-400 text-lg"
          />

        </motion.div>

      ) : (

        <FaRegCircle
          className="text-slate-600 text-lg"
        />

      )}

      {/* Text */}

      <motion.span

        animate={{
          color: completed
            ? "#4ade80"
            : active
            ? "#ffffff"
            : "#64748b",
        }}

        className="text-sm"

      >

        {stage}

      </motion.span>

    </motion.div>

  );

}