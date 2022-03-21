import React, { useState, useEffect, Component } from "react";
import { Link } from "react-router-dom";
import { useParams } from "react-router-dom";
import { ReactComponent as ArrowLeft } from "../assets/arrow-left.svg";
import { useNavigate } from "react-router-dom";
import { useHistory } from "react-router";
import axios from "axios";
import SignOut from "../SignOut";
class Test extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fileName: "",
      fileContent: "",
    };
  }

  //   NotePage = () => {
  //     // let params = useParams();
  //     console.log("Khoa Dang");
  //     const history = useNavigate();
  //     const { id } = useParams();
  //     let [note, setNote] = useState(null);
  //     useEffect(() => {
  //       getNote();
  //     }, [id]);

  //     let getNote = async () => {
  //       if (id === "new") return;
  //       let response = await fetch(`/api/notes/${id}/`);
  //       let data = await response.json();
  //       setNote(data);
  //     };

  //     let createNote = async () => {
  //       console.log("KhoaTI");
  //       fetch(`/api/notes/create/`, {
  //         method: "POST",
  //         headers: {
  //           "Content-Type": "application/json",
  //         },
  //         body: JSON.stringify(this.content),
  //       });
  //     };
  //   };

  handleFileChange = (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.readAsText(file);
    reader.onload = () => {
      this.setState({ fileName: file.name, fileContent: reader.result });
      const content = this.state.fileContent;
      console.log(content);
      console.log("ti");

      let CreateNote = async () => {
        let formField = new FormData();
        formField.append("content", content);
        formField.append("name", "tit");
        formField.append("action", "create-post");
        await axios({
          method: "POST",
          url: "/api/product/create/",
          data: formField,
        }).then((response) => {});

        // fetch(`/api/notes/create/`, {
        //   method: "POST",
        //   headers: {
        //     "Content-Type": "application/json",
        //   },
        //   body: JSON.stringify(content),
        // })
        //   .then((response) => response.json())

        // console.log("Khoa Pham Dang ti");
      };
      CreateNote();
    };
    reader.onerror = () => {
      console.log("file error", reader.error);
    };
  };

  render() {
    return (
      <div>
        <h1> File Reader</h1>
        <input type='file' onChange={this.handleFileChange}></input>
        <br />
        {/* <button onClick={this.NotePage}>Done</button> */}

        <p>{this.state.fileName}</p>
        <p>{this.state.fileContent}</p>
        <SignOut/>
      </div>
    );
  }
}

export default Test;
