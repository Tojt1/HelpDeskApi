import Tickets from "../components/Tickets.jsx";

<div className="dasboard-container">

                <h2>Hello {users.name}</h2>

                <form onSubmit={SubmitDash} className="dashboard-form">

                    <p>Jakiego rodzaju jest twój problem?</p>
                    <input
                    type="text"
                    placeholder="....."
                    value={problemTitle}
                    onChange={(e) => setProblemTitle(e.target.value)}/>

                    <p>Opisz swój problem</p>
                    <input
                    type="text"
                    placeholder="....."
                    value={problemDescription}
                    onChange={(e) => setProblemDescription(e.target.value)}/>

                    <p>Z jakiej kategori jest twój problem</p>
                    <input
                    type="text"
                    placeholder="Category...."
                    value={problemCategory}
                    onChange={(e)=> setProblemCategory(e.target.value)}/>

                    <button type="submit" className="dashboard-btn">Wyślij ticket</button>
                </form>
            </div>