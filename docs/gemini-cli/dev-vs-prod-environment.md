## `dev` vs `prod` environment

Our release flows support both `dev` and `prod` environments.

The `dev` environment pushes to a private Github-hosted NPM repository, with the
package names beginning with `@google-gemini/**` instead of `@google/**`.

The `prod` environment pushes to the public global NPM registry via Wombat
Dressing Room, which is Google's system for managing NPM packages in the
`@google/**` namespace. The packages are all named `@google/**`.

More information can be found about these systems in the
[NPM Package Overview](/docs/npm)