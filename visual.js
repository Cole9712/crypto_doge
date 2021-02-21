// sparkline visualization

const mykey = process.env.NOMICS_API_KEY;
//const mykey = 'demo-6410726746980cead2a17c9db9ef29af';
const fetch = require( "node-fetch" );

function getSparkline( id, s, e )
{
	let reqUrl = "https://api.nomics.com/v1/currencies/sparkline?";
	let key = "key=" + mykey;
	let ids = "&ids=" + id;
    let start = "&start=" + s + "T00%3A00%3A00Z";
    let end = "&end=" + e + "T00%3A00%3A00Z";


	fetch( reqUrl + key + ids + start + end )
		.then( res =>
		{
			if( res.status !== 200 )
			{
				return null;
		 	}
			else
			{
				res.json();
			}
		} )
		.then( data => { return( data ) } );
}
console.log("hi");
console.log( getSparkline( 'BTC', "2021-02-10", "2021-02-20" ) );

function visual()
{

}
