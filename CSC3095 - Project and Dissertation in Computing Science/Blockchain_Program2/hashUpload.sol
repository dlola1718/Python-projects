pragma solidity ^0.4.21;
pragma experimental ABIEncoderV2;
contract HashUpload {
    mapping(string => string) fileHash;
    string[] fileList;
    
    
    function storeHash(string fileName, string hashOfFile){
        fileHash[fileName] = hashOfFile;
        fileList.push(fileName);
        }
    
    //...Retrieve hash of file //
    function retrieve(string fileName) public view returns (string){
        return fileHash[fileName];
    }
    
   // ... retrieve previous blocks : Retrieve name of files sent to Blockchain //
    function showAllFileNames() public view returns (string[]){
        return fileList;
    }
}