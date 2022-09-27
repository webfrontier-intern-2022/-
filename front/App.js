import React from "react";
import axios from "axios";

function App() {
	const [data, setData] = React.useState();
	const url = "http://127.0.0.1:8000";

	const GetData = () => {
		axios.get(url).then((res) => {
			setData(res.data);
		});
	};
	return (
		<div>
			    <div className="App">
    <header><h1>ログイン画面</h1></header>
    <p>メールアドレス</p>
    <input type="1text" value="01234@webfronier.ac.jp"></input>
    <p>パスワード</p>
    <input type="2text" value="****"></input>
    <p></p>
    </div>
		{data ? <div><a href='URL'><button onClick={GetData}>ログイン</button></a></div> : <button onClick={GetData}>ログイン</button>}
	</div>
	);
}