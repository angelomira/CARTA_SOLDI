const https = require('https');
const fs = require('fs');

const file = fs.createWriteStream("DATA.csv");
const request = https.get("https://query1.finance.yahoo.com/v7/finance/download/AMZN?period1=1680054836&period2=1711677236&interval=1d&events=history&includeAdjustedClose=true", function(response) {
   response.pipe(file);
   file.on("finish", () => {
       file.close();
       console.log("Download Completed");
   });
});