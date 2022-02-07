#### CAP concept
- distributed system has three significant characteristics: Consistency, Availability, Partition tolerance.
- They can't be existed same time, assume: G1,G2 are servers, client. since:
  - **Partition tolerance** can't be avoided because the information can be transfer errors.
  - [e.g.](https://www.ruanyifeng.com/blog/2018/07/cap.html) when G1 transfer info to G2. If keeps consistency, G2 should be locked and can't be wrote, which means that the availability is not accessble.
- usually choose C over A, sometimes A maybe not that latest and updated later.
- 
- 
