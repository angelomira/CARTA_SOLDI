const fs = require('fs-extra');

(async () => {
    const data = (await fs.readFile('DATA.csv', { encoding: 'utf-8' })).split('\n');

    const headers = data[0].split(',');

    console.info(headers);

    const header_id = headers.indexOf('High');

    let parsed_data = data.slice(1);

    for(let i = 0; i < parsed_data.length; i++) {
        parsed_data[i] = parsed_data[i].split(',')[header_id];
    }

    console.info(parsed_data);
})();