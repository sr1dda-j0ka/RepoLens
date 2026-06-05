import { GitBranchPlus } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="
      flex
      justify-between
      items-center
      px-8
      py-5
      border-b
      border-slate-800
    ">
      <h1 className="text-2xl font-bold text-blue-500">
        RepoLens
      </h1>

      <GitBranchPlus className="cursor-pointer" />
    </nav>
  );
}