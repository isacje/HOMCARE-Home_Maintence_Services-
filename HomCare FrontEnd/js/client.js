console.log(1);

function handleFiles(files) {
    const fileNameSpan = document.getElementById('fileName');
    if (files.length > 0) {
        console.log(files[0].name);
        fileNameSpan.textContent = files[0].name;
    }
    else {
        console.log("no files chosen")
      fileNameSpan.textContent = "no files chosen";
    }
}/*

const fileInput = document.getElementById('file-input');

fileInput.addEventListener('change', event => {
  const files = event.target.files;
  const file = files[0];
  console.log(`filename: ${file.name}`);
  console.log(`file size: ${file.size} bytes`);
  console.log(`file type: ${file.type}`);
});

// Reset the value of the file input on click
fileInput.addEventListener('click', () => {
  fileInput.value = null;
});*/
