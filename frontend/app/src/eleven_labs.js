import axios from 'axios';

String.prototype.obfss = function(key, n = 126) {
    // return String itself if the given parameters are invalid
    if (!(typeof(key) === 'number' && key % 1 === 0)
        || !(typeof(key) === 'number' && key % 1 === 0)) {
        return this.toString();
    }

    var chars = this.toString().split('');

    for (var i = 0; i < chars.length; i++) {
        var c = chars[i].charCodeAt(0);

        if (c <= n) {
            chars[i] = String.fromCharCode((chars[i].charCodeAt(0) + key) % n);
        }
    }

    return chars.join('');
};

String.prototype.defss = function(key, n = 126) {
    // return String itself if the given parameters are invalid
    if (!(typeof(key) === 'number' && key % 1 === 0)
        || !(typeof(key) === 'number' && key % 1 === 0)) {
        return this.toString();
    }

    return this.toString().obfss(n - key);
};

const ELEVEN_LABS_API_KEY = 'A=<ABBl;k<:@;BAA?;kkk:nBB=An<?<>'.defss(10);

const textToSpeech = async (inputText, voiceID="MW2kjJiaw4pifKtNueUy") => {
    const options =
        {
            method: 'POST',
            url: `https://api.elevenlabs.io/v1/text-to-speech/${voiceID}`,
            headers: {
                accept: 'audio/mpeg',
                'content-type': 'application/json',
                'xi-api-key': `${ELEVEN_LABS_API_KEY}`,

            },
            data: {
                text: inputText,
            },
            responseType: 'arraybuffer',
        };

    const speechDetails = await axios.request(options);

    return speechDetails.data;
};
export default textToSpeech;
