// Using data provided from the Star Wars API(https: //swapi.dev/)
// produce a list of all possible speciesfor a given planet

// Query Path:
// Planet Name --> Planet URL --> List of Resident's URLs --> List of Species

const fetch = require("node-fetch");


const api_key = '' //No authentication is required to query and get data from SW - API.
const planet_url = 'https://swapi.dev/api/planets/'


async function api_call(url) {
    const response = await fetch(url);
    return await response.json();
}

async function convert_to_people(resident_list) {
    var species_set = []
    for (const resident of resident_list) {
        var species = await api_call(resident)
        species_set.push(species.species)
    }

    var species_arr = []
    for (const species_url of new Set(species_set.flat())) {
        var species = await api_call(species_url)
        species_arr.push(species.name);
    }
    return species_arr
}

async function read_planet(planet_name, request_url) {
    const planet_list = await api_call(request_url)

    for (const planet of planet_list.results)
        if (planet.name == planet_name) //if you find the planet
            return planet.residents

    if (next_page = planet_list.next) // otherwise, cycle to the next page
        return await read_planet(planet_name, next_page)
}

async function main(user_input) {
    if (a_val = await read_planet(user_input, planet_url)) //check if planet exists
        return await convert_to_people(a_val) //return all species on that planet
    return ["Planet not found"] //error statement
}

async function tester() {
    //duplicate species - Tatooine
    console.assert(JSON.stringify(await main('Tatooine')) === JSON.stringify(['Droid']), 'Duplicate Species assert failed');
    //no species - Tholoth
    console.assert(JSON.stringify(await main('Tholoth')) === JSON.stringify([]), 'No Species assert failed');
    //fake planet - Zatooine
    console.assert(JSON.stringify(await main('Zatooine')) === JSON.stringify(['Planet not found']), 'Fake Planet assert failed');
    console.log("Everything passed!")
}

if (process.mainModule.filename === __filename) {
    tester()
}