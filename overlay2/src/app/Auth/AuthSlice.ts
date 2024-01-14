import {createSlice} from "@reduxjs/toolkit";

interface IProfile {
  email: string
}

interface IAuthState {
  token: string | null;
  refreshToken: string | null,
  profile?: IProfile,
  loading: boolean,
  error: boolean,
  authenticated: boolean
}

const initialState: IAuthState = {
  authenticated: false, error: false, loading: false, refreshToken: null,
  token: null
}
export const Index = createSlice({
  name: "auth",
  initialState,
  reducers: {

  }
})