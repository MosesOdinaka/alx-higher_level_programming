#!/urs/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurence');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
