# TypeScript Compiler

Now that we know so much about what TypeScript syntax looks like, we will learn about the TypeScript compiler. The objectives of this lesson are:

1. Installing and using the TypeScript compiler
2. Viewing compiled JS output for TS code
3. Understanding the configuration and use of the compiler config file

## What is a compiler?

In case you haven't heard about "compilers" before or are unsure about the term, A compiler is a special program that translates a programming language's source code into machine code, bytecode or another programming language. The source code is typically written in a high-level, human-readable language such as Java or C++. A programmer writes the source code in a code editor or an integrated development environment (IDE) that includes an editor, saving the source code to one or more text files. A compiler that supports the source programming language reads the files, analyzes the code, and translates it into a format suitable for the target platform.

Sometimes the term "transpiler" is used interchangeably with compiler, but they are not exactly the same. Transpilers, or source-to-source compilers, are tools that read the sourcecode written in one programming language and produce the equivalent code in another programming language with a similar level of abstraction. And TypeScript is a good example of transpiler as it converts TypeScript code to JavaScript. Similarily, Babel transpiler can also be used for converting the ES6 JS code to ES5 JS sourcecode. Compilers also convert the code from one language to other language but both languages are very different in abstraction level. For example, Java compiler converts the `.java` file to `.class` file.

Strictly speaking, TypeScript is _transpiled_ to JavaScript. However, most developers and Microsoft iteself refers to the tool that does this as "TypeScript Compiler". That said, don't fret too much about the loose usage of the term compiler and compilation. As long as what's actually happening is clear from the context, it doesn't really matter which term is used — the message still gets through. Transpilers are also called source-to-source compilers, so "TypeScript Compiler" could also be considered short for "TypeScript to JavaScript Compiler".

## Installing and using the compiler

To install and start using the TypeScript Compiler or tsc on your machine, you can do a global npm package installation.

```bash
npm i -g typescript
```

Then you can verify the installation by checking for the compiler version.

```bash
tsc -v
```

Now you can start writing TypeScript code in any `.ts` file. Let's say you wrote some code in a file called `index.ts`. All you need to do in order to compile to JavaScript is:

```bash
tsc index
```

You will see that TypeScript creates a JS file of the same name `index.js` with the transpiled JS code. If there were any errors found during compilation, they would get flagged in the terminal. But if you're using a modern editor like VSCode, you can find errors being flagged by the IDE itself and even auto-complete recommendations showing up to prevent you from making type errors.

You can open up the transpiled JS file and read through the code. Depending on how complex your TS file was or how many lines of code it had, the transpiled JS file may or may not be easily readable. But just a skim through the generated JS files still gives an idea of how the TypeScript Compiler works.

You can also simply run the command `tsc` if you have more than one target TS file to be compiled and it will automatically search for TS files in the project folder and transpile them. You can also run TypeScript Compiler in watch mode using `tsc --watch` and it will watch for file changes, re-compile and hot reload.

## TypeScript Compiler Configuration

TypeScript uses a configuration file in the project folder to follow any custom rules or options you would like to set. To generate this file, just run:

```bash
tsc --init
```

This will immediately create a `tsconfig.json` file in your project folder. You'll see that this file contains a property called `compilerOptions` with lots and lots of options mostly commented out. You can read through the comments or visit the TypeScript docs to learn about these options, but no need to worry about memorizing these. In most of your projects, you might have to adjust just a few properties here and there.

```json
{
  "compilerOptions": {
    "module": "commonjs",
    "esModuleInterop": true,
    "target": "es6",
    "noImplicitAny": true,
    "moduleResolution": "node",
    "sourceMap": true,
    "outDir": "dist",
    "baseUrl": ".",
    "paths": {
      "*": ["node_modules/*"]
    }
  },
  "include": ["src/**/*"]
}
```

For example, you might see the `target` property is set by default to `"es5"`. This results in `var` being used in the output JS files. You may change this to `"es6"` to enable use of `let` and `const` and other ES6 syntax.

You can configure the `outDir` and `rootDir` properties and provide paths to your desired output directory and input directory. So then you could have a `src` directory and `dist` directory in your project structure to separate source code and production code.

## Conclusion

You can read up more about the `tsconfig.json` file [here](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html) but it is really not that complicated. This lesson intends to give you an idea about how the TypeScript compiler works and you can possibly visualize a little bit of what is happening under the hood. You can also find many online TypeScript IDEs, playgrounds and compilers that let you try out TS code and view the compiled JS output, [here](https://www.codingrooms.com/compiler/typescript) is one. We will now move into looking at TypeScript in practice with Node and Express.

---

## References

- https://www.techtarget.com/whatis/definition/compiler
- https://howtodoinjava.com/typescript/transpiler-vs-compiler/
- https://www.youtube.com/watch?v=BCg4U1FzODs&t=669s&ab_channel=TraversyMedia
