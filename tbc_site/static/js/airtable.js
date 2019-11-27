import Airtable from 'airtable';
// EXAMPLE USING ENVIRONMENT VARIABLE
// # Shell:
// $ export AIRTABLE_API_KEY=keyCDI9g6pLU2Le5i

// # Node:
// const base = require('airtable').base('app2OXtbMVkriy7KX');
// EXAMPLE USING CUSTOM CONFIGURATION
// var Airtable = require('airtable');
Airtable.configure({
	endpointUrl: 'https://api.airtable.com',
	apiKey: 'keyCDI9g6pLU2Le5i'
});
var base = Airtable({apiKey: 'keyCDI9g6pLU2Le5i'}).base('app2OXtbMVkriy7KX');

base('Department').select({
	// Selecting the first 3 records in Main View:
	maxRecords: 3,
	view: "Main View"
}).eachPage(function page(records, fetchNextPage) {
	// This function (`page`) will get called for each page of records.

	records.forEach(function(record) {
		console.log('Retrieved', record.get('Name'));
	});

	// To fetch the next page of records, call `fetchNextPage`.
	// If there are more records, `page` will get called again.
	// If there are no more records, `done` will get called.
	fetchNextPage();

}, function done(err) {
	if (err) { console.error(err); return; }
});

