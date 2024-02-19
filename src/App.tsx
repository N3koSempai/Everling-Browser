import { Button, Input,MenuHandler, Menu, MenuItem, MenuList } from "@material-tailwind/react";
import "./App.css"
import { useState } from "react"

function App() {
  const [searchValue, setSearchValue] = useState('https://www.youtube.com')
  const [fixedSearch, setFixedSearch] = useState('')


const fixedSearchFormat = () => {
  const httpFormat = /^http:\/\//
  const httpsFormat = /^https:\/\//
  const googleQuery = 'https://www.google.com/search?igu=1&ei=&q='
  if (httpFormat.test(searchValue) || httpsFormat.test(searchValue)) {
    setFixedSearch(searchValue)
  } else {
setFixedSearch(`${googleQuery}${searchValue}` )
  }

}

  return (
<div className=" flex flex-col" style={{width: '100%'  ,height: '100vh'}}>
  
  <div className="NavBar flex flex-row items-center mt-2 w-full lg:h-[5%] h-[10%] justify-center" >
  <div className="self-start w-[30%]" />
    <div className="flex w-[50%] flex-row  items-center justify-center  ">
         <Input value={searchValue} onChange={(e) => setSearchValue(e.target.value)} size="lg" variant="outlined"  placeholder="Search" id='searchBard' crossOrigin={''}/>
         <Button placeholder='' color="blue" className='ml-2'onClick={()=>{fixedSearchFormat()}}>search </Button>
    </div>
    <div className="w-[25%]"/>
    <div className="NavBarMenu  self-center justify-center items-center mr-2 ">
      <Menu>
        <MenuHandler>
        <Button placeholder=''>Menu</Button>
      </MenuHandler>
      <MenuList placeholder='' className="items-center justify-center">
        <MenuItem className="text-center" placeholder=''>Preference</MenuItem>
        <MenuItem className="text-center" placeholder=''>style</MenuItem>
        <MenuItem className="text-center" placeholder=''>about me</MenuItem>
      </MenuList>
      </Menu>
    </div>
    
    
    
  </div>
  <div className="w-full h-full  mt-2" style={{ borderRadius: '1.5rem 1.5rem 0 0', borderImage: 'linear-gradient(to right, blue, red) 1', borderWidth: '0.4rem 0 0 0', borderStyle: 'solid'  }}>

    <iframe title="Main Webview" 
  sandbox="allow-modals allow-top-navigation-by-user-activation allow-same-origin allow-scripts allow-popups allow-forms"
   loading="lazy" referrerPolicy="unsafe-url"
  src={fixedSearch} className="w-full h-full" />
      </div> 
</div>
  )
}

export default App



