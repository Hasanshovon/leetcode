https://leetcode.com/problems/symmetric-tree/description/?envType=problem-list-v2&envId=tree

### General Notes on Recursive and Iterative Approaches

When solving problems like **101. Symmetric Tree** or similar problems involving tree traversal or comparisons, you have the choice between **iterative** and **recursive** approaches. Understanding the relationship between the two can help you decide which is best for your specific problem and style of coding.

- **Iterative Approach with Stack**:  
  In an iterative approach, a **stack** is used to simulate the function call stack that recursion would otherwise handle automatically. The stack stores the state of your computation (like nodes in a tree), and a `while` loop processes these nodes. For problems involving tree traversals or comparisons (like checking symmetry), the stack helps to keep track of which nodes need to be revisited later, allowing you to "pop" the last node off the stack and continue processing. The logic for pushing and popping nodes mimics what happens during a recursive call.

- **Recursive Approach**:  
  In contrast, recursion automatically handles this process using the **call stack** of the program. Each time you make a recursive call, the current state of the function (including parameters and local variables) is pushed onto the stack. The base case of recursion provides the condition under which the function returns, ending the current frame of execution. The recursive calls then handle the next part of the problem, similar to how the stack handles further operations in an iterative loop.

### Key Observations on Recursion vs. Iteration:

- **Recursion can be more intuitive**: Problems like tree traversal or symmetry are often naturally recursive in nature. The problem of symmetry directly suggests a recursive solution because each subtree must mirror another subtree.
- **Recursion is simpler but may run into depth issues**: Recursive code tends to be simpler and shorter because the function calls themselves handle a lot of the work (stack management, tracking the state). However, recursion can be problematic if your tree is very deep, as Python has a limit on the depth of recursion (although this is rarely an issue for moderate-sized trees).
- **Iteration avoids recursion depth limits**: Iterative solutions using a stack avoid the recursion depth limit and can handle deep trees better. They tend to be slightly longer and more complex because you have to explicitly manage the stack, but they work just as effectively.

### Tricks to Solve Problems Like 101. Symmetric Tree

1. **Understand the Symmetry Condition**:
   For a tree to be symmetric, its left and right subtrees must be mirror images of each other:

   - The root values must match.
   - The left child of the left subtree must match the right child of the right subtree, and vice versa.
   - If one side is `None`, the other side must also be `None`.

2. **Key Recursive Idea**:

   - The recursive function takes two nodes as input, comparing them at each step.
   - If both nodes are `None`, they are symmetric.
   - If one node is `None` but the other isn’t, the tree isn’t symmetric.
   - If both nodes exist, compare their values and recursively check their subtrees (left child with the opposite right child).

3. **Key Iterative Idea**:

   - Use a **stack** or **queue** to iteratively simulate the recursive process.
   - Push pairs of nodes onto the stack (or queue) for comparison.
   - Pop nodes off, compare them, and if they match, push their children (in mirrored order) onto the stack for further comparison.
   - Continue until the stack (or queue) is empty, and if no mismatches are found, the tree is symmetric.

4. **Optimize for Early Exits**:
   In both approaches, return `False` immediately when a mismatch is found. This saves unnecessary comparisons. Whether in recursion or iteration, your first focus should be finding mismatches as soon as possible to make the algorithm efficient.

5. **Visualize Recursion and Stack**:
   If you're new to recursion, it helps to visualize the function calls as a tree themselves. Each recursive call branches off to more recursive calls, and once a base case is reached, the function starts returning results back up the tree. For iteration, think of the stack as controlling how deep into the tree you've gone.

6. **Handle Edge Cases**:
   - **Empty Tree**: An empty tree (where `root` is `None`) is symmetric by definition.
   - **Single Node Tree**: A tree with only a root node and no children is symmetric.
   - **Unequal Subtrees**: If one subtree has more nodes than the other (in terms of structure, not just values), the tree cannot be symmetric.

- **Recursion**:
  - Think of recursion as a natural way to solve problems involving trees or mirrored structures.
  - Focus on identifying the base case, then build your recursive calls by mirroring the structure of the problem (in this case, compare the left and right subtrees recursively).
- **Iteration**:

  - If you prefer avoiding recursion depth issues or want more control over the state, use a stack to simulate recursion.
  - Push nodes onto the stack in a mirrored order, and compare pairs as you pop them off.

- **Debugging**:
  - For recursion, add print statements to trace the recursive calls.
  - For iteration, inspect the contents of your stack to see what nodes are being processed.
