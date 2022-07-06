import React from "react";
import { useState, useEffect, useRef } from "react";
import {PaperAirplaneIcon} from "@heroicons/react/outline"
import "../style/Messenger.css"

export default function Messenger(params) { 
    const scrollRef = useRef(); // for auto scrolling
    // conversations stock all conversations
    // TODO: save persistence on disk
    const [conversations, setConversations] = useState([]);
    const onSentMessage = (event) => {
        // This function is actioned when user sent message
        //
        const today = new Date();
        // const date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
        const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        //const dateTime = date+' '+time;
        const user_uttered = document.getElementById("input_message").value;
        setConversations(
            [...conversations, {id: "user_uttered", text: user_uttered, createdAt: time}]
        )
        document.getElementById("input_message").value = ""
    }

    useEffect(() => {
        // Auto scrolling 
        scrollRef.current?.scrollIntoView({ behavior: "smooth" });
      }, [conversations]);

    const onPressEnter = (event) => {
        if(event.code === "Enter"){
            onSentMessage(event)
        }
    }

       
    return (       
        <div className="bg-gray-200 p-5 flex justify-center h-5/6">
            <div className="bg-gray-100 w-1/2 flex flex-col shadow-2xl rounded-xl">
                <div id="output_message" className="rounded-t-2xl flex-1 overflow-y-scroll scroll-auto p-5">
                   
                </div>
                <div className="flex p-3 bg-slate-500" >
                        <input
                        id="input_message"
                        className="w-full p-3 flex-1 rounded-3xl"
                        type="text"
                        name="input"
                        placeholder="Message..."
                        onKeyUp={onPressEnter}
                        />
                    <div onClick={onSentMessage} >
                        <PaperAirplaneIcon className="rounded-2xl h-12 rotate-90 cursor-pointer pl-1" />
                    </div>
                </div>
            </div>
        </div>
    )
}