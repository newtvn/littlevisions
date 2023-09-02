import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "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",
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

