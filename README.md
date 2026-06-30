 #### Short Reflection

# What was the easiest concept to understand?
The easiest part for me was learning how to use describe() and it() blocks to structure my tests. It makes perfect sense to group related tests inside a describe block and use the it blocks for individual actions. I also found basic commands like cy.visit(), cy.click(), and cy.type() very simple and straightforward to understand because they just mirror exactly how a real human clicks and types on a web page

# What was the most challenging?
The most challenging part was definitely dealing with unexpected website errors and timeouts. Sometimes my code was completely correct, but the tests would still fail because the website loaded too slowly or had background JavaScript errors that crashed the Cypress runner. It was frustrating trying to find the right CSS selectors when real websites kept changing their layouts or blocking automated tools with tracking scripts. Learning how to use error shields to bypass these random crashes took a lot of trial and error
