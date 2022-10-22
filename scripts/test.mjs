#!/usr/bin/env zx

const command = process.argv[3] ? `${process.argv[3]}_test.py` : "index.py";
const commands = process.argv.slice(4, process.argv.length);

await $`python ./tests/${command} ${commands}`;
