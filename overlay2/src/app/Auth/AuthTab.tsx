// From https://gist.github.com/gauravtiwari/2ae9f44aee281c759fe5a66d5c2721a2
// By https://gist.github.com/gauravtiwari

const loginTab = (myUrl: string) => {
  const windowArea = {
    width: Math.floor(window.outerWidth * 0.8),
    height: Math.floor(window.outerHeight * 0.5),
  };

  if (windowArea.width < 1000) {
    windowArea.width = 1000;
  }
  if (windowArea.height < 630) {
    windowArea.height = 630;
  }

  const sep = myUrl.indexOf("?") !== -1 ? "&" : "?";
  const url = `${myUrl}${sep}`;
  const windowOpts = `toolbar=0,scrollbars=1,status=1,resizable=1,location=1,menuBar=0,
      width=${windowArea.width},height=${windowArea.height}`;

  const authWindow = window.open(url, "_blank", windowOpts);
  // Listen to message from child
  return new Promise((resolve, reject) => {
    window.addEventListener(
      "onmessage",
      (msg: any) => {
        if (
          !~msg.origin.indexOf(
            `${window.location.protocol}//${window.location.host}`
          )
        ) {
          if(authWindow){
            authWindow.close();
          }
          reject("Not allowed");
        }

        if (msg.data.auth) {
          try {
            resolve(JSON.parse(msg.data.auth));
          } catch (e) {
            resolve(msg.data.auth);
          } finally {
            if (authWindow){
              authWindow.close();
            }

          }
        }
        if (msg.data.error) {
          reject(msg.data.error);
        }
      },
      false
    );
  });
};

export default loginTab;
