import axios from 'axios';

const ELEVEN_LABS_API_KEY = 'c2c3d59e0e449b3bd370a8d717636f1c'

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
