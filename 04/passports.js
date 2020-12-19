
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

    let count1 = 0;
    let count2 = 0;

    fs.readFileSync('input', 'utf-8').split('\n\n').forEach(passport => {
        if (!required_fields.every(field => {
            return passport.includes(field + ':')
        })) {
            return;
        } else {
            count1++;
        }

        if (passport.split('\n').join(' ').split(' ').every(field => {
            let f, v
            [f, v] = field.split(':')

            switch (f) {
                case 'byr': {
                    if (v.length != 4) {
                        return false
                    }
                    if (isNaN(v)) {
                        return false
                    }
                    return parseInt(v) >= 1920 && parseInt(v) <= 2002
                }
                case 'iyr': {
                    if (v.length != 4) {
                        return false
                    }
                    if (isNaN(v)) {
                        return false
                    }

                    return parseInt(v) >= 2010 && parseInt(v) <= 2020
                }
                case 'eyr': {
                    if (v.length != 4) {
                        return false
                    }
                    if (isNaN(v)) {
                        return false
                    }
                    return parseInt(v) >= 2020 && parseInt(v) <= 2030
                }
                case 'hgt': {
                    let unit = v.slice(-2)
                    let n = v.slice(0, -2)
                    if (isNaN(n)) {
                        return false
                    }
                    if (unit == 'cm') {
                        return (parseInt(n) >= 150 && parseInt(n) <= 193)
                    } else if (unit == 'in') {
                        return (parseInt(n) >= 59 && parseInt(n) <= 76)
                    } else {
                        return false
                    }
                }
                case 'hcl': {
                    if (!v.startsWith('#')) {
                        return false;
                    }

                    let chars = v.slice(1)
                    if (chars.length != 6) {
                        return false;
                    }

                    return !isNaN(parseInt(chars, 16))
                }
                case 'ecl': {
                    const valid = [
                        'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
                    ]

                    return valid.some(ecl => { return v == ecl })
                }
                case 'pid': {
                    if (v.length != 9) {
                        return false
                    }
                    return !isNaN(parseInt(v))
                }

                default:
                    return true;
            }
        })) {
            count2++;
        }
    });

    console.log(`There are ${count1} passports containing all required fields`)
    console.log(`There are ${count2} valid passports`)

})()
