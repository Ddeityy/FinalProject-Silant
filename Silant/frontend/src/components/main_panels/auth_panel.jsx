import React from "react";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import AuthMaitenanceTable from "../tables/auth_maitenance_table.jsx";
import AuthRepairTable from "../tables/auth_repair_table.jsx";
import AuthCarTable from "../tables/auth_car_table.jsx";
import "./tabs.css";

const AuthPanel = () => {
    return (
        <div>
            <Tabs>
                <TabList>
                    <Tab>Машины</Tab>
                    <Tab>ТО</Tab>
                    <Tab>Рекламации</Tab>
                </TabList>
                <TabPanel>
                    <AuthCarTable />
                </TabPanel>
                <TabPanel>
                    <AuthMaitenanceTable />
                </TabPanel>
                <TabPanel>
                    <AuthRepairTable />
                </TabPanel>
            </Tabs>
        </div>
    );
};
export default AuthPanel;
