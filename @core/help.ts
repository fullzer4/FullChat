const printHelp = (): void => {
  console.log(`Usage: notesynk [OPTIONS...]`);
  console.log("\nOptional flags:");
  console.log("  -h, --help                Display this help and exit");
  console.log("  -s, --save                Save your notes");
  console.log("  -f, --folder              Set your folder to synk");
  console.log("  -t, --timeout             Set the timeout to synk");
}

export default printHelp
