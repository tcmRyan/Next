'use client'
import React, {useEffect, useState} from "react";
import {Box, Card} from "@mui/material";
import axios from "axios";

const UpNext = () => {
  const [items, setItems] = useState<any[]>([])

  useEffect(() => {
    axios.get("")
  }, []);

  const cards = items.map((item, i) => {
    return <Card key={i}></Card>
    }

  )

  return (
    <div>
      <Box style={{position: "absolute", width: "25%", left: "0px", backgroundColor: "black", height: "100%", borderColor: "red", borderWidth: "3px"}}>
        <ul>

        </ul>
      </Box>
    </div>
  )
}

export default UpNext;