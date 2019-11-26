$(document).ready(function(){

    // Random country name array
    const countries = ['Natish', 'Eastern Maarland', 'Tonianor', 'Dadwi', 'Irki', 'Genaire Stinebar',
        'Seecan Ryniacook', 'Gerchristcroa', 'Republic of Tintiau', 'Ina', 'Northern Ito Landpasta', 'Tuca Isles',
        'Runne Moma', 'Bermo Greendo', 'Lapitvirpalva', 'Isle of Riae Coko', 'Suslandsre', 'Niretui', 'Lyca Walporein',
        'Thenganitedmomor', 'Theldogypt', 'Gigasumibul', 'Canldives Grecoca', 'Macos Quenianau',
        'Central Toxem Ofnordesh', 'Francele Mary', 'Repu', 'Domland Frilau Republic', 'Mii Lands', 'Mua Norngo',
        'United Southjan', 'Andczech', 'Letan', 'North Lklandco', 'Naguiingcu', 'Nonsland Viaguiru',
        'Slandsi Ofcen Island', 'Cothe Siana', 'Andba Frenchslands', 'Umyher', 'Legin', 'Amebra', 'Geri Massada',
        'Razue Lands', 'Thernstates', 'Myanseypados', 'Landstan Sintsloni', 'Tito Territories', 'Rupo Auchique',
        'Sternmayotte Giumvina', 'Guaso', 'Serco', 'Soco Maau', 'Kittsten Guernntsercairn', 'United Decar Rasriki',
        'Southlu Vaoutcoast', 'Belti Saintrusni', 'Vietslands Lianion', 'Blicbe', 'Laosye Guiriblic', 'Landdi Nitedman',
        'Terla Tobyana', 'North Blicni', 'Nilombiablicguastan', 'Slonela', 'Northern Ntarcbo Nakhstan', 'Basope', 'Apu',
        'Guayre', 'Martar Rusigui', 'Finnei Dunamo', 'Gharat Nuaba', 'Lasteinsa', 'Jebritish Isnti', 'Guamstan Lands',
        'Caili Era', 'New Menmevo', 'Zstankia', 'Galcao', 'Pumau Coica', 'Lyri', 'Tazer', 'Diantic Kerastates',
        'Ancro Beminew', 'Geslands Andzamki', 'Standor', 'Riturksnkababwe', 'Mofrench Gabesaint', 'Frenchof Saintluxi',
        'Dorblic Engslandskeeling Territories', 'Haigylaneastria', 'Zilswibru', 'Northern Ngaroeli', 'Haratedsri',
        'Igan', 'Reraqntinehong', 'Stoeblic', 'Riland', 'United Iu Abu', 'Senicra', 'Nachi Saunguilzim', 'Janis',
        'Stinelands', 'Beva', 'Eo', 'Eastern Roonfaslewalespa', 'Stadi Inliahrain', 'Raki', 'Coye Dore', 'Voniani',
        'Insland', 'Mishall Morswa', 'Dorblic Ingostan', 'Iofnew', 'Loupenia Ghaastan', 'Ribya Renti', 'Northmac Iue',
        'Aandhe Land', 'Coblic Andand', 'Norsouth Sokongnew', 'Dinesnkalandriapu', 'Mikhstan Jaimark', 'Rida',
        'Kaand Artu', 'Biaslandsmailu', 'Irus Siatozam', 'Britishkiaxemman', 'Strathern', 'Slandsde', 'Manbenited',
        'South Denstansouthruna', 'Theco', 'Guagin Sainttarland', 'Beco Leve', 'Lislands Territories', 'Kiberza Land',
        'Dofi', 'Danandine', 'Statesrethua', 'Lekyrre', 'Ugaslyki', 'Ganremac', 'Ratedsal', 'Zecia', 'Volandne',
        'Gatarbia', 'Costa Donon Tazea', 'Bardcra Imaba', 'Titvia Stange', 'Rakraine Walmauno', 'Modisu', 'Maland',
        'Ibo Evislo', 'Landthern Pierretzer', 'Virlauda', 'Brazi', 'Sialand', 'Nainntarc', 'Netic Pitstates',
        'Sternluofia', 'Catral Magreece', 'Nakona', 'Nevia', 'Moarat', 'Virdad', 'Sniathai Souboura', 'Nionlau Iliagua',
        'Uly Treaelblic', 'Maland Punin', 'Mihu Gianauna Land', 'South Quenea', 'Marnia', 'Frimi', 'Kepia Isona',
        'Tusa', 'Ratesmoaco', 'Rialrocgua', 'Statesakucro', 'Andstonitedru Land', 'Ridian', 'Idorspain',
        'Western Siermaii', 'Cole', 'Saupri Liasia', 'Papa Faly', 'Armosaori', 'Denu', 'Outchristslands', 'Blicla',
        'Manor Vacumon', 'Central Svalcaqua', 'Care Nitednia', 'Pani', 'Goma', 'Trilom Daporeguya', 'Costa Nibacan',
        'Zbesaint Raqblic', 'Central Aldivespuer', 'Randeba', 'Tiante'];

    // Insert random country into input
    document.getElementById('country_name').value = countries[Math.floor(Math.random() * countries.length)];




     // Catch button click event
    $("#submit").on('click', function(){

        // Prevent default redirects
        event.preventDefault();

        // Place loading icon and empty meter
        document.getElementById('output').outerHTML = '<div id="output" class="loading loading-lg"></div>';
        document.getElementById('meter').outerHTML = '<div id="meter"></div>';

        // Ajax call to prediction
        $.ajax({
            url: 'predict?' + $.param({
                x: document.querySelector('#infant_mortality_rate').value,
                y: document.querySelector('#malaria_mortality_rate').value,
                z: document.querySelector('#wash_mortality_rate').value,
                year: document.querySelector('#prediction_year').value}),
            type: 'POST',
            contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
            success: function (response) {

                // Replace loading icon with response data
                document.getElementById('output').outerHTML = '<span class="h3" id="output"><mark>' + response + ' years</mark></span>';
                document.getElementById('meter').outerHTML = '<meter id="meter" class="meter" value="' + response +'" optimum="85" min="40" max="80" low="50" high="80"></meter>';

                // Find average life expectancy and the response difference
                const average_expectancy = 65;  //TODO
                const expectancy_diff = (response - average_expectancy) / average_expectancy * 100;

                // Insert a new row at the top of the table
                let newRow = document.getElementById('log').insertRow(1);

                // Insert cells into the new row
                let nameCell = newRow.insertCell(0);
                let valueCell = newRow.insertCell(1);
                let relativeCell = newRow.insertCell(2);

                // Append to cells
                nameCell.appendChild(document.createTextNode(document.querySelector('#country_name').value));
                valueCell.appendChild(document.createTextNode(response));
                relativeCell.appendChild(document.createTextNode(expectancy_diff.toFixed(3) + '%'));

                // Add new data to graph
                 barChart.addData([40], "Google");

                // Insert random country into input
                document.getElementById('country_name').value = countries[Math.floor(Math.random() * countries.length)];

                },
            error: function() {
                document.getElementById('output').outerHTML = '<span class="text-error">There was an error!</span>';
            }
        });
    });
});