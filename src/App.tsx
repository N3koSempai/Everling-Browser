/* <div id='WebViewFramer' className="flex flex-col h-[50%] w-full mt-4 overflow-x-hidden overflow-y-scroll" >

</div> */
import { Button, Input } from "@material-tailwind/react";
import "./App.css";

import { useState } from "react"
import Frame from "./components/frame"
function App() {
  const [searchValue, setSearchValue] = useState('https://www.wikipedia.com')
  const [fixedSearch, setFixedSearch] = useState('')


  return (
    <div className="container flex flex-col" style={{width: '100%'  ,height: '100vh'}}>
      <div className="flex w-[100%] h-[10%] items-center justify-center" >

    <div className="flex w-[50%] flex-row  items-center justify-center text-center">
      <Input value={searchValue} onChange={(e) => setSearchValue(e.target.value)} size="lg" variant="outlined"  placeholder="Search" id='searchBard' crossOrigin={''}/>
      </div>
      <Button placeholder='' color="blue" className='ml-2'onClick={()=>{setFixedSearch(searchValue)}}>search </Button>
      </div>
      <Frame src={fixedSearch} />
      
    </div>
  );
}

export default App;
