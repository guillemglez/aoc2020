
(function () {

    const fs = require('fs')

    const required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ];

    let count = 0;

    fs.readFileSync('input', 'utf-8').split('\n\n').forEach(passport => {
        if (required_fields.every(field => {
            return passport.includes(field + ':')
        })) {
            count++
        }
    });

    console.log(`There are ${count} valid passports`)

})()
