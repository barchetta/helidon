
# Releasing Helidon

These are the steps for doing a release of Helidon.

# Overview

The Helidon release workflow is triggered when a change is pushed to
a branch that starts with `release-`. The release workflow performs
a Maven release to the Nexus staging repository. It does not currently
do a GitHub release, so you must do that manually using a script. Here
is the overall flow:

1. Create a local release branch.
2. Update CHANGELOG and update version if needed.
3. Push release branch to remote, release workflow runs.
4. Verify bits in Nexus staging repository and then release them.
5. Create GitHub release.
6. Update CHANGELOG in `main` (or in maintenance branch), and possibly SNAPSHOT version.
7. Verify release source tag is there, then drop `release-x.y.z` branch

# Steps in detail

```
# Set this to the version you are releasing
export VERSION="x.y.z"
# Branch to release: main, helidon-3.x, helidon-2.x, etc
export BRANCH_TO_RELEASE="main"
```

1. Create local release branch
    ```
    git clone git@github.com:oracle/helidon.git
    # Make sure we have latest
    git fetch
    git checkout -b release-${VERSION} origin/${BRANCH_TO_RELEASE}
    # Make sure we have what we think we have
    git log
    ```
2. Update local release branch
   1. Update `CHANGELOG.md`
      1. Create new section for the `x.y.z` release
      2. Update new section with latest info
      3. Add release to dictionary at bottom of CHANGELOG
      4. Commit changes locally. It's useful to have CHANGELOG update in separate commit for later cherry-pick.
   2. Update version if needed. Inspect top level pom. Then if needed:
      `etc/scripts/release.sh --version=${VERSION}-SNAPSHOT update_version`. Then commit changes.
   3. `git log` to make sure you have what you think you have.
   4. If you updated version then do a quick test build: `mvn clean install -DskipTests`

3. Push local release branch to remote. This will trigger a release workflow in GitHub Actions.

    ```
    git push origin release-${VERSION}
    ```

4. Wait for the release workflow in Actions to complete: https://github.com/helidon-io/helidon/actions/workflows/release.yaml.

5. Check nexus staging repository
    1. In browser go to: https://oss.sonatype.org/#view-repositories and login as helidonrobot.
    2. On left click "Staging Repositories"
    3. Scroll down list of repositories and find `iohelidon-`. It should be Status closed.
    4. A common failure in the release build is a Bad Gateway from oss.sonatype.org. If that happens
       drop the bad staging repository and re-run the release workflow in GitHub Actions.
    
6. Test staged bits    
    1. Do quick smoke test by trying an archetype that is in the staging
       repo (see staging repository profile at end of this document)
    
        ```
        mvn -U archetype:generate -DinteractiveMode=false \
            -DarchetypeGroupId=io.helidon.archetypes \
            -DarchetypeArtifactId=helidon-quickstart-se \
            -DarchetypeVersion=${VERSION} \
            -DgroupId=io.helidon.examples \
            -DartifactId=quickstart-se \
            -Dpackage=io.helidon.examples.quickstart.se \
            -Possrh-staging
        
        cd quickstart-se
        
        mvn package -Possrh-staging
        ```
        
    2. Do full smoke test using test script (this requires staging profile to be configured):
       ```
       smoketest.sh --giturl=https://github.com/helidon-io/helidon.git --version=${VERSION} --clean --staged full
       ```
    3. The smoketest script will leave its work in `/var/tmp/helidon-smoke.XXXX`.
       Go there, into the quickstarts and test the native builds.
       
6. Release repository: Select repository then click Release (up at the top)
   1. In description you can put something like "Helidon x.y.z Release"
   2. It might take a while (possibly hours) before the release appears in Maven Central
   3. To check on progress look at https://repo1.maven.org/maven2/io/helidon/helidon-bom/
       
6. Create GitHub release
   1. Create a fragment of the change log that you want used for the release
      description on the GitHub Releases page. Assume it is in `frag.md`
   2. Set your API key (you generate this on your GitHub Settings):
      ```
      export GITHUB_API_KEY=<longhexnumberhere.....>
      ```
   3. Run script to create release in GitHub:
      ```
      etc/scripts/github-release.sh --changelog=./frag.md --version=${VERSION}
      ```
   4. Go to https://github.com/helidon-io/helidon/releases and verify release looks like
      you expect. You can edit it if you need to.

7. Update CHANGELOG (and possibly version) in main (or the branch you released).
   1. Create post release branch: `git checkout -b post-release-${VERSION}`
   2. Copy CHANGELOG from your release branch and commit (or cherry-pick commit).
   3. Update SNAPSHOT version number to the next release (in 4.x we stopped doing this for every dot-dot release)
      ```
      etc/scripts/release.sh --version=x.y.zz-SNAPSHOT update_version
      ```
   4. Add and commit changes then push
      ```
      git push origin post-release-${VERSION}
      ```
   5. Create PR and merge into master

8. Verify the release source tag exists: https://github.com/helidon-io/helidon/releases/tag/${VERSION}, 
   then remove `release-${VERSION}` branch from https://github.com/helidon-io/helidon
9. Updating website is outside the scope of this README

# Staging Repository Profile

To pull artifacts from the sonatype staging repository add this profile to your `settings.xml`:

```
      <profile>
           <id>ossrh-staging</id>
           <activation>
               <activeByDefault>false</activeByDefault>
           </activation>
           <repositories>
               <repository>
                   <id>ossrh-staging</id>
                   <name>OSS Sonatype Staging</name>
                   <url>https://oss.sonatype.org/content/groups/staging/</url>
                   <snapshots>
                       <enabled>false</enabled>
                   </snapshots>
                   <releases>
                       <enabled>true</enabled>
                   </releases>
               </repository>
           </repositories>
           <pluginRepositories>
               <pluginRepository>
                   <id>ossrh-staging</id>
                   <name>OSS Sonatype Staging</name>
                   <url>https://oss.sonatype.org/content/groups/staging/</url>
                   <snapshots>
                       <enabled>false</enabled>
                   </snapshots>
                   <releases>
                       <enabled>true</enabled>
                   </releases>
               </pluginRepository>
           </pluginRepositories>
       </profile>
```
