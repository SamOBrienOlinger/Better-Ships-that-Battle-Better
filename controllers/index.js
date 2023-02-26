const options = {};

// options.ip = '127.0.0.1';
options.port = parseInt(process.env.PORT);

var type = process.argv.indexOf('--release', 1) !== -1 || process.argv.indexOf('release', 1) !== -1 ? 'release' : 'debug';
// require('total4/' + type)(options);
require('total4').http('release', options);