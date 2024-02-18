import React from "react";

interface IFrameProps {
  src: string;
}

const Frame: React.FC<IFrameProps> = ({ src }) => {
  return <iframe title="internal Webview" src={src} className="w-[100%] h-[100%]" />;
};

export default Frame