<h1>Installation Guide — cross_paths</h1>
<p>This document explains how to install the cross_paths module globally on Python 3.13 using pip, including installation from a folder, path, or sub-module.</p>
<h2>Requirements</h2>
<ul>
<li>Python 3.7+</li>
<li>pip</li>
<li>Valid project layout</li>
</ul>
<p>Your directory should follow this structure:</p>
<pre><code class="language-markdown">cross_paths/
├─ pyproject.toml
└─ cross_paths/
└─__init__.py
</code></pre>
<h3>Minimal pyproject.toml for cross_paths:</h3>
<pre><code class="language-toml">[project]
name = "cross_paths"
version = "0.1.0"
requires-python = ">=3.8"
</code></pre>
<h2>Installation Methods</h2>
<ol>
<li><strong>Editable install (recommended during development)</strong>
<pre><code class="language-bash">cd /path/to/cross_paths
pip install -e .
</code></pre>
</li>
<li><strong>Normal install (copies files into site-packages)</strong>
<pre><code class="language-bash">cd /path/to/cross_paths
pip install .
</code></pre>
</li>
<li><strong>Install using absolute path</strong>
<pre><code class="language-bash">pip install /absolute/path/to/cross_paths
</code></pre>
</li>
<li><strong>Install directly from Git</strong>
<pre><code class="language-bash">pip install git+https://github.com/you/your_repo.git
</code></pre>
</li>
</ol>
<h3>Installing as a sub-module inside another repo</h3>
<p>If cross_paths is stored inside a project directory:</p>
<pre><code class="language-markdown">project/
└─ tools/
└─ cross_paths/
</code></pre>
<p>Install it directly by pointing pip to the sub-folder:</p>
<pre><code class="language-bash">pip install project/tools/cross_paths
</code></pre>
<p>For standalone usability, ensure that <code>cross_paths/tools/cross_paths/</code> contains its own pyproject.toml as shown above.</p>
<h2>Verification</h2>
<p>Confirm the module is installed and reachable by Python 3.13:</p>
<pre><code class="language-bash">python3.13 -c "import cross_paths; print(cross_paths.file)"
</code></pre>
<p>Expected result: a valid path to the installed package.</p>
<h2>Notes</h2>
<ul>
<li>pyproject.toml is the preferred build config for Python 3.13.</li>
<li>Global installs may require admin rights depending on your system.</li>
<li>While editable installs are convenient for development, use a normal install when publishing or distributing.</li>
</ul>
