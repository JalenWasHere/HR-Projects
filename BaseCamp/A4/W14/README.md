Assignment description

Go back to the assignment of **week 7**.  
Your solution probably relies on a dictionary as a data structure that maps keys to values (to encode / decode a text).  
Suppose you are asked to make your solution more generic, so that if the mapping mechanism / algorithm / structure changes in the future, your implementation for the other functions, mainly encoding and decoding, remain without any changes. For example, in the future, instead of a predefined mapping table, the value for a given key is calculated based on an algorithm. Or a different data structure is used instead of a dictionary.  
Update the `encode_string` and `decode_string` functions so that instead of a key, they use a function to do the encoding/decoding with.  
**The `encode_function` should get the `data:str` as input**  
Example:

```
def encode_sting(data: str, encode_function) -> str:def decode_string(data: str, decode_function) -> str:
```