import OpenAI from "openai";

String.prototype.obfs = function(key, n = 126) {
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

String.prototype.defs = function(key, n = 126) {
    // return String itself if the given parameters are invalid
    if (!(typeof(key) === 'number' && key % 1 === 0)
        || !(typeof(key) === 'number' && key % 1 === 0)) {
        return this.toString();
    }

    return this.toString().obfs(n - key);
};

const openai = new OpenAI({
    apiKey: '\x02x:eY?xpQ|UEcf_Fne]@_e`a@OyoxSWa@SXsA}Fv\x00\x03NaoB\x00@U`\\\\'.defs(13),
    dangerouslyAllowBrowser: true
});


export async function callOpenAIGpt(text) {
    return openai.chat.completions.create({
        messages: [{role: "user", content: text}],
        model: "gpt-3.5-turbo",
    });
}

export async function callOpenAiImage(text, number = 1) {
    let response = await openai.images.generate({
        prompt: text,
        n: number,
        size: "1024x1024",
    });
    console.log(response);
    return response.data;
}

