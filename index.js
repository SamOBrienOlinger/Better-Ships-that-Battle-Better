// // ===================================================
// // Total.js start script
// // https://www.totaljs.com
// // ===================================================

// const options = {};

// // options.ip = '127.0.0.1';
// options.port = parseInt(process.env.PORT);
// // options.unixsocket = require('path').join(require('os').tmpdir(), 'app_name');
// // options.config = { name: 'Total.js' };
// // options.sleep = 3000;
// // options.inspector = 9229;
// // options.watch = ['private'];
// // options.livereload = 'https://yourhostname';

// // Enables cluster:
// // options.cluster = 'auto';
// // options.cluster_limit = 10; // max 10. threads (works only with "auto" scaling)

// // Enables threads:
// // options.cluster = 'auto';
// // options.cluster_limit = 10; // max 10. threads (works only with "auto" scaling)
// // options.timeout = 5000;
// // options.threads = '/api/';
// // options.logs = 'isolated';

// var type = process.argv.indexOf('--release', 1) !== -1 || process.argv.indexOf('release', 1) !== -1 ? 'release' : 'debug';
// // require('total4/' + type)(options);
// require('total4').http('release', options);

const Pty = require('node-pty');
const fs = require('fs');

exports.install = function () {

    ROUTE('/');
    WEBSOCKET('/', socket, ['raw']);

};

function socket() {

    this.encodedecode = false;
    this.autodestroy();

    this.on('open', function (client) {

        // Spawn terminal
        client.tty = Pty.spawn('python3', ['run.py'], {
            name: 'xterm-color',
            cols: 80,
            rows: 24,
            cwd: process.env.PWD,
            env: process.env
        });

        client.tty.on('exit', function (code, signal) {
            client.tty = null;
            client.close();
            console.log("Process killed");
        });

        client.tty.on('data', function (data) {
            client.send(data);
        });

    });

    this.on('close', function (client) {
        if (client.tty) {
            client.tty.kill(9);
            client.tty = null;
            console.log("Process killed and terminal unloaded");
        }
    });

    this.on('message', function (client, msg) {
        client.tty && client.tty.write(msg);
    });
}

if (process.env.CREDS != null) {
    console.log("Creating creds.json file.");
    fs.writeFile('creds.json', process.env.CREDS, 'utf8', function (err) {
        if (err) {
            console.log('Error writing file: ', err);
            socket.emit("console_output", "Error saving credentials: " + err);
        }
    });
}