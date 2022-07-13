import "../style/Message.css";
import userLogo from "../assets/user-icon.png";
import djamo from "../assets/djamo.png";
import ReactMarkdown from "react-markdown";
//import { format } from "timeago.js";
import base_url from "../constant";
function Message({ text, audio, createdAt, own }) {
  if (own) {
    if (text) {
      return (
        <div className="message own">
          <div className="messageTop">
            <p className="messageText">
              <ReactMarkdown>{text}</ReactMarkdown>
            </p>
            <img className="messageImg" src={userLogo} alt="" />
          </div>
          <div className="messageBottom">{createdAt}</div>
        </div>
      );
    } else {
      return (
        <div className="message own">
          <div className="messageTop">
            <audio id="audio" controls src={audio.url}></audio>
            <img className="messageImg" src={userLogo} alt="" />
          </div>
          <div className="messageBottom">{createdAt}</div>
        </div>
      );
    }
  } else {
    // const audio_to_play = new Audio()
    // var blob = new Blob([audio], { type: 'audio/mp3' })
    // var url = window.URL.createObjectURL(blob)
    // console.log(blob)
    // audio_to_play.src = url
    // audio_to_play.play()

    return (
      <div className="message">
        <div className="messageTop">
          <img className="messageImg" src={djamo} alt="" />
          <div>
            <p className="messageText">
              <ReactMarkdown>{text}</ReactMarkdown>
            </p>
            {audio && <audio
              id="audio"
              controls
              autoPlay
              src={`${base_url}/assets/recording/${audio}`}
            ></audio>}
          </div>
        </div>
        <div className="messageBottom">{createdAt}</div>
      </div>
    );
  }
}
export default Message;
