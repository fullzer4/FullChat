import parseArguments from "./@core/parser.ts"
import printHelp from "./@core/help.ts"

const main = (inputArgs: string[]): void => {

  const args = parseArguments(inputArgs);

  if (args.help) {
    printHelp();
    Deno.exit(0);
  }

  let save: boolean = args.save;

  console.log(args);
  console.log(save)

}

main(Deno.args)
