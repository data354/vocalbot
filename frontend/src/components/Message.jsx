import "../style/Message.css";
import userLogo from "../assets/user-icon.png"
import djamo from "../assets/djamo.png"
import ReactMarkdown from "react-markdown";


function Message({text, createdAt, own }) {
  if (own){
    return (
            <div className="message own">
                <div className="messageTop">
                    <p className="messageText"><ReactMarkdown>{text}</ReactMarkdown></p>
                    <img
                    className="messageImg"
                    src={userLogo}
                    alt=""
                    />
                </div>
                <div className="messageBottom">{createdAt}</div>
            </div>
        )
  } else{
    return (
        <div className="message">
        <div className="messageTop">
            <img
            className="messageImg"
            src={djamo}
            alt=""
            />
            <p className="messageText"><ReactMarkdown>{text}</ReactMarkdown></p>
        </div>
        <div className="messageBottom">{createdAt}</div>
        </div>
    )
  }
}
export default Message;