import "../style/App.css";
import Footer from "./Footer";
import Nav from "./Nav";
import Messenger from "./Messenger";

function App() {
  return (
    <div className="bg-slate-800 h-screen">
      <Nav />
      <Messenger />
      <Footer />
    </div>
  );
}

export default App;
