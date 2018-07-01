pragma solidity ^0.4.24;

 
contract ERC20 {
  function transfer(address to, uint value) public returns (bool);
  function balanceOf(address who) public view returns (uint256);
}

contract Ownable {
    address public owner;

    constructor() public {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function transferOwnership(address _newOwner) public onlyOwner {
        require(_newOwner != address(0));
        owner = _newOwner;
    }
}

contract AirDrop is Ownable {
    address public owner;

    function () public payable {}

    function withdraw() public onlyOwner {
        msg.sender.transfer(address(this).balance);
    }

    function deliver(address _tokenAddr, address[] _to, uint256[] _value, uint32 total) public onlyOwner
    returns(bool _succ)
    {
        require(_to.length == total);
        require(_value.length == total);
        require(total <= 256);
        
        for (uint8 i = 0; i < _to.length; i++) {
            assert((ERC20(_tokenAddr)).transfer(_to[i], _value[i]));
        }
        return true;
    }
}
